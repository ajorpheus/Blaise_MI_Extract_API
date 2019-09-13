pipeline { 
    agent any
    stages {
        stage('PullDockerImage') {
            steps {
               sh '''
               ls
               pwd
               sh DockerPull.sh
               '''
           }
       }
    }
}
