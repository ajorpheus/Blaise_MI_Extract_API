pipeline { 
    agent any
    stages {
        stage('PullDockerImage') {
            steps {
               sh '''
               pwd
               ls
               sh DockerPull.sh
               '''
           }
       }
    }
}
