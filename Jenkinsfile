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
                sh 'docker login -u '
                withCredentials([usernamePassword( credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    usr = USERNAME
                    pswd = PASSWORD
                }
                sh 'docker login -u ${usr} -p ${pswd}'
                sh 'docker push tchit/jenkins-flask:${BUILD_NUMBER}'
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
