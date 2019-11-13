pipeline {
  //build the local Dockerfile
  agent { dockerfile true }
  stages {
    stage('build') {
      steps {
        sh 'ttcn3_start /home/titan/playground/mqtt/iottestware.mqtt /home/titan/playground/mqtt/BasicConfig.cfg'
      }
    }
  }
}
