pipeline { 
    agent any
    stages {
        stage('PullDockerImage') {
            steps {
               sh '''docker pull onsdigital/blaise-mi-extract-api:latest'''
           }
       }
    }
}
