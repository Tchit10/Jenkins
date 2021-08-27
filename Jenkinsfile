pipeline {
    environment { 
        registry = "tchit/jenkins-flask" 
        registryCredential = 'dockerhub'
        dockerImage = '' 
    }
    agent any
   
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script { 
                    dockerImage = docker.build(registry + ":$BUILD_NUMBER", "./flask/Dockerfile")
                }
                //sh 'docker info'
                //sh 'docker build -t tchit/jenkins-flask:${BUILD_NUMBER} ./flask'
                //sh 'docker tag tchit/jenkins-flask:${BUILD_NUMBER} tchit/jenkins-flask:latest'
                //sh 'docker images'
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
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                }
            }
        }
        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $registry:$BUILD_NUMBER" 
            }
        } 
    }
}
