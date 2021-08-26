pipeline {
    agent {
        docker { image 'dind' }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'docker info'
                sh 'docker build -t tchit/jenkins-flask:${BUILD_NUMBER} ./flask'
                sh 'docker tag tchit/jenkins-flask:${BUILD_NUMBER} tchit/jenkins-flask:latest'
                sh 'docker images'
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
