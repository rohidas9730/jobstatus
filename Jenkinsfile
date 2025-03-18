pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'rohidas9730'
        DOCKER_HUB_PASSWORD = 'rohidas@123'
        DOCKER_IMAGE_BACKEND = 'rohidas9730/quantum:backendjob'
        DOCKER_PS_BACKEND = 'backendjob'
        DOCKER_IMAGE_FRONTEND = 'rohidas9730/quantum:frontendjob'
        DOCKER_PS_FRONTEND = 'frontendjob'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'git-private-tocken', url: 'https://github.com/rohidas9730/jobstatus.git'
            }
        }

        stage('Build Docker Image and Deploy') {
            steps {
                script {
                    sh "docker-compose up --build -d"
                }
            }
        }

        stage('login and push Docker image') {
            steps {
                script {
                    sh 'dockerlogin -u ${DOCKER_HUB_USERNAME} -p ${DOCKER_HUB_PASSWORD}'
                    sh 'docker push ${DOCKER_IMAGE_BACKEND}'
                    sh 'docker push ${DOCKER_IMAGE_FRONTEND}'
                }
            }
        }

        stage('logout docker hub') {
            steps {
                script {
                    sh 'dockerlogout'
                }
            }
        }
    }

    post {
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Deployment failed!"
        }
    }
}
