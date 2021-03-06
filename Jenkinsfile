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
                    dockerImage = docker.build(registry + ":$BUILD_NUMBER", "./flask")
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
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $registry:$BUILD_NUMBER" 
            }
        } 
        stage('Ansible') {
            steps {
                ansiblePlaybook become: true, becomeUser: 'debian', credentialsId: 'private-key', disableHostKeyChecking: true, installation: 'Ansible', inventory: 'inventory.yml', playbook: 'playbook.yml', limit: 'all'
            }
        }
    }
}
