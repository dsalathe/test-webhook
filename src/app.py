#!flask/bin/python
import os
import shutil
from flask import Flask, jsonify, request, render_template
from pprint import pprint
from git import Repo

import models
import db

from compile import compileDir
app = Flask(__name__)

GIT_FOLDER = './git'


def clone_branch(repoUrl, folder, branchRef, branchName):
    Repo.clone_from(repoUrl, folder)
    repo = Repo(folder)
    origin = repo.remotes['origin']
    origin.fetch(branchRef)
    git = repo.git
    git.checkout(branchName)


@app.route('/pull-request', methods=['POST'])
def check_code():
    # pprint(request.json)
    if request.json['action'] in ['opened', 'edited', 'synchronize']:
        requestID = request.json['number']
        requestLabel = request.json['pull_request']['head']['label']
        requestRef = request.json['pull_request']['head']['ref']
        requestStatusUrl = request.json['pull_request']['_links']['statuses']['href']
        if not os.path.exists(GIT_FOLDER):
            os.makedirs(GIT_FOLDER)
        else:
            shutil.rmtree(GIT_FOLDER)
            os.makedirs(GIT_FOLDER)
        clone_branch(request.json['pull_request']['base']['repo']['clone_url'], GIT_FOLDER, 'pull/' + str(requestID) + '/head:' + requestRef, requestRef)

        # pendingResPayload = { 'state': 'pending' }
        # pendingRes = requests.post(requestStatusUrl, json = pendingResPayload)

        # compile code and run tests
        print('Compiling...')
        compilationResult = compileDir(GIT_FOLDER + '/src')
        if compilationResult:
            print('Compilation succeeded.')
        else:
            print('Compilation failed.')

    #    if compilationResult == True:
    #        successResPayload = { 'state': 'success' }
    #        requests.post(requestStatusUrl, json = successResPayload)
    #    else:
    #        failureResPayload = { 'state': 'failure' }
    #        requests.post(requestStatusUrl, json = failureResPayload)
        return 'Compiling'
    return 'Not Compiling'


@app.route('/builds', methods=['GET'])
def show_builds():
    """
    Queries all the builds from the database and renders the list view with all builds
    :return: rendered template
    """
    builds = models.Builds.query.all()
    return render_template('builds.html', data=builds)


if __name__ == '__main__':
    db.init_db()  # database initialization
    app.run(debug=True, port=8014)  # run the application on port 8014
