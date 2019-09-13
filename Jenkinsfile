pipeline { 
    agent any
    stages {
        stage('PullDockerImage') {
           steps {
               sh DockerPull.sh
           }
       }
    }
}
