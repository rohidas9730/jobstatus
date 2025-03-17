pipeline
  egent any
  stages {
    stage('clone repo') {
       steps {
          git branch: 'main', credentialsId: 'git-private-tocken', url: 'https://github.com/rohidas9730/jobstatus.git'
       }
    }
    stage('build docker image and deploy') {
      steps {
        script {
          sh "docker-compose up --build"
        }
      }
    }
post {
  success {
    echo "Deployment successfull!"
  }
  failure {
    echo "Deployment Failed!"
  }
}
}
          
