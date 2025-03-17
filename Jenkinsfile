pipeline {
    agent any

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
