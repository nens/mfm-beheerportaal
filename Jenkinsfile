pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                checkout scm
                sh "mkdir -p var/static var/media var/log"
                sh "rm -rf .venv"
                sh "echo 'COMPOSE_PROJECT_NAME=${env.JOB_NAME}-${env.BUILD_ID}' > .env"
                sh "docker --version; docker-compose --version"
            }
        }
        stage("Build") {
            steps {
                sh "docker-compose down --volumes"
                sh "docker-compose build --build-arg uid=`id -u` --build-arg gid=`id -g` web"
                sh "docker-compose run --rm --volume $HOME/.netrc:/home/nens/.netrc --volume $HOME/.cache:/home/nens/.cache web pipenv install --deploy --dev"
                sh "docker-compose run --rm web pip freeze"
            }
        }
        stage("Check") {
            steps {
                sh "docker-compose run --rm web pipenv check"
            }
        }
        stage("Test") {
            steps {
                sh "docker-compose run --rm web python manage.py test"
            }
        }
        stage("Flake 8") {
            steps {
                sh "if docker-compose run --rm web flake8 mfm_beheerportaal > flake8.txt; then echo 'flake8 is a success'; else cat flake8.txt; false; fi"
            }
        }
    }
    post {
        always {
            sh "docker-compose down --volumes --remove-orphans && docker-compose rm -f && rm -rf .venv"
        }
    }
}
