pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                docker info
                docker build -t tchit/jenkins-flask:${BUILD_NUMBER} ./flask
                docker tag tchit/jenkins-flask:${BUILD_NUMBER} tchit/jenkins-flask:latest
                docker images
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
