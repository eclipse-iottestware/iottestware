pipeline {
  //build the local Dockerfile
  agent { dockerfile true }
  stages {
    stage('build') {
      steps {
        sh 'mkdir build'
        sh 'cp -R /home/titan/playground/mqtt build'
      }
    }
  }
  post {
    always {
      echo "Starting to archive ..."
      archiveArtifacts artifacts: 'build/**/*.*', fingerprint: true
    }
  }
}
