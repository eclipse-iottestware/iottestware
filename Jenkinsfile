pipeline {
  //build the local Dockerfile
  agent { dockerfile true }
  environment {
  	RELEASE='0.1.0'
  }
  stages {
    stage('build') {
      steps {
        sh 'mkdir -p release-${RELEASE}/iottestware'
        sh 'cp -R /home/titan/playground/* release-${RELEASE}/iottestware'
        dir('performance')
        {
        	git 'https://github.com/eclipse/iottestware.performance'
        } 
	dir('fuzzing')
	{
		git 'https://github.com/eclipse/iottestware.fuzzing'
	}
	dir('docs')
	{
		sh 'wget -O iottestware-v${RELEASE}.pdf readthedocs.org/projects/iottestware/downloads/pdf/latest'
	}
	sh 'cp -R performance fuzzing docs release-${RELEASE}/iottestware'
      }
    }
  }
  post {
    always {
      echo "Starting to archive ..."
      archiveArtifacts artifacts: 'release-0.1.0/**/*', fingerprint: true
      cleanWs()
    }
  }
}
