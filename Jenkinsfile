pipeline { 
    agent any
    stages {
        stage('PullDockerImage') {
            steps {
               sshagent(credentials: ['blaisejenkinstest']) {
                   sh 'ssh -o StrictHostKeyChecking=no iqbals1@blaisedk-d-01 uptime'
                   sh 'ls'
               }
           }
       }
    }
}
