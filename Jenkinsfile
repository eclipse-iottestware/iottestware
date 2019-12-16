pipeline {
  //build the local Dockerfile
  agent { dockerfile true }
  stages {
    stage('build') {
      steps {
        sh 'rm -rf build'
        sh 'mkdir build'
        sh 'cp -R /home/titan/playground/* build'
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
