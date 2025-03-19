pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'rohidas9730'
        DOCKER_HUB_PASSWORD = 'rohidas@123'
        DOCKER_IMAGE_BACKEND = 'quantum/backendjob:latest'
        DOCKER_PS_BACKEND = 'backendjob'
        DOCKER_IMAGE_FRONTEND = 'quantum/frontendjob:latest'
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
                    sh 'docker stop ${DOCKER_PS_BACKEND}'
                    sh 'docker stop ${DOCKER_PS_FRONTEND}'
                    sh 'docker rm ${DOCKER_PS_BACKEND}'
                    sh 'docker rm ${DOCKER_PS_FRONTEND}'
                    sh "docker-compose up --build -d"
                }
            }
        }

        stage('login and push Docker image on DockerHub') {
            steps {
                script {
                    sh 'docker login -u ${DOCKER_HUB_USERNAME} -p ${DOCKER_HUB_PASSWORD}'
                    sh 'docker push ${DOCKER_IMAGE_BACKEND}'
                    sh 'docker push ${DOCKER_IMAGE_FRONTEND}'
                }
            }
        }

        stage('logout docker hub') {
            steps {
                script {
                    sh 'docker logout'
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
