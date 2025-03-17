pipeline
  egent any
  stages {
    stage('clone repo') {
       steps {
          git branch: 'main', credentialsId: 'git-private-tocken', url: 'https://github.com/rohidas9730/jobstatus.git'
       }
    }
    stage('build docker image') {
      steps {
        script {
          sh "docker build -t backendjob ."
        }
      }
    }
    stage('Deploy Container') {
      steps {
        script {
          sh "docker stop backendjob || true"
          sh "docker rm backendjob || true"
          sh "docker run -d -p 8000:8000 --name backendjob backendjob"
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
          
