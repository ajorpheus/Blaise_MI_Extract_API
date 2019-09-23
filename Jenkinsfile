pipeline { 
    agent any
    stages {
        stage('PullDockerImage') {
            steps {
               sshagent(credentials: ['blaisejenkinstest']) {
                   sh 'ssh -o StrictHostKeyChecking=no s_Balise5_Dev@blaisedk-d-01'
                   sh 'ssh -v s_Balise5_Dev@blaisedk-d-01'
                   sh 'ls'
               }
           }
       }
    }
}
