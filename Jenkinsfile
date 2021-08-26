pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                docker info
                docker build -t tchit/jenkins:${BUILD_NUMBER} .
                docker tag tchit/jenkins:${BUILD_NUMBER} tchit/jenkins:latest
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
