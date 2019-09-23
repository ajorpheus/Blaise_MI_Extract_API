pipeline {
 agent any
 stages {
  stage('PullDockerImage') {
   steps {
    sshagent(credentials: ['cb4dd465-9f1b-42a5-b78b-dd3594949e3c']) {
     shh 'ssh -o StrictHostKeyChecking=no s_Blaise5_Dev@blaisedk-d-01 uptime'
     sh 'ls'
    }
   }
  }
 }
}
