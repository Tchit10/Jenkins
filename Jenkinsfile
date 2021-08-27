pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'docker info'
                sh 'docker build -t tchit/jenkins-flask:${BUILD_NUMBER} ./flask'
                sh 'docker tag tchit/jenkins-flask:${BUILD_NUMBER} tchit/jenkins-flask:latest'
                sh 'docker images'
                docker.withRegistry( 'tchit/jenkins-flask', 'dockerhub' ) {
                    dockerImage = 'tchit/jenkins-flask:${BUILD_NUMBER}'
                    dockerImage.push()
                }
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
