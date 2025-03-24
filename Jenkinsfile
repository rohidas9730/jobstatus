pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'rohidas9730'
        DOCKER_HUB_PASSWORD = 'rohidas@123'
        DOCKER_IMAGE_BACKEND = 'backendjob'
        DOCKER_PS_BACKEND = 'backendjob'
        DOCKER_IMAGE_FRONTEND = 'frontendjob'
        DOCKER_REPO = 'quantum'
        DOCKER_PS_FRONTEND = 'frontendjob'
        VULNARABILITY_FILE = 'vulnarabilityfile.txt'
        EMAIL_ID = 'rohidasmugale@gmail.com'
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

        stage('login and push Docker image on DockerHub') {
            steps {
                script {
                    sh "echo '${DOCKER_HUB_PASSWORD}' | docker login -u '${DOCKER_HUB_USERNAME}' --password-stdin"
                    sh 'docker tag ${DOCKER_IMAGE_BACKEND} ${DOCKER_HUB_USERNAME}/${DOCKER_REPO}:${DOCKER_IMAGE_BACKEND}'
                    sh 'docker tag ${DOCKER_IMAGE_FRONTEND} ${DOCKER_HUB_USERNAME}/${DOCKER_REPO}:${DOCKER_IMAGE_FRONTEND}'
                    sh 'docker push ${DOCKER_HUB_USERNAME}/${DOCKER_REPO}:${DOCKER_IMAGE_BACKEND}'
                    sh 'docker push ${DOCKER_HUB_USERNAME}/${DOCKER_REPO}:${DOCKER_IMAGE_FRONTEND}'
                }
            }
        }
        
        stage('install trivy for scan images') {
            steps {
                script {
                    sh '''
                    echo "ubuntu" | sudo -s apt-get install wget apt-transport-https gnupg lsb-release mailutils -y
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
echo "ubuntu" | sudo -S apt-get update
echo "ubuntu" | sudo -S apt-get install trivy -y

                    '''
                }
            }
        }

        stage('scan docker image') {
            steps {
                script { 
                    sh '''
                    trivy image ${DOCKER_IMAGE_FRONTEND} > ${VULNARABILITY_FILE}
                    '''
                }
            }
        }

        stage('vulnarability report send to mail') {
            steps {
                script {
                    sh '''
                    echo "vulnarabilty report" | mail -s "image scan report" -A ${VULNARABILITY_FILE} ${EMAIL_ID}
                    '''
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
