pipeline {
  //build the local Dockerfile
  agent { dockerfile true }
  stages {
    stage('build') {
      steps {
        sh 'rm -rf build'
        sh 'mkdir build'
        sh 'cp -R /home/titan/playground/* build'
        dir('iottestware.performance')
        {
          git 'https://github.com/eclipse/iottestware.performance'
        } 
				dir('iottestware.fuzzing')
				{
				  git 'https://github.com/eclipse/iottestware.fuzzing'
				}
				sh 'cp -R iottestware.performance iottestware.fuzzing build'
      }
    }
  }
  post {
    always {
      echo "Starting to archive ..."
      archiveArtifacts artifacts: 'build/**/*', fingerprint: true
    }
  }
}
