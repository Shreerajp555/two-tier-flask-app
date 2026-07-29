pipeline{
    agent {label "dev"}
    stages{
        stage("Code Clone"){
            steps{
                git url: "https://github.com/Shreerajp555/two-tier-flask-app.git", branch: "main"
            }
        }
        stage("Build Stage"){
            steps{
                sh "docker build -t two-tier-flask-app:latest ."
            }
        }
        stage("TEST"){
            steps{
                echo "Testing team will do test"
            }
        }
        stage("Push to DockerHub"){
            steps{
                withCredentials([usernamePassword(credentialsId:"dockerHubCreds",
                passwordVariable: "dockerHubPass",
                usernameVariable: "dockerHubUser"
                )]){
                sh "docker login -u ${env.dockerHubUser} -p ${dockerHubPass}"
                sh "docker image tag two-tier-flask-app:latest ${dockerHubUser}/two-tier-flask-app:latest"
                sh "docker push ${env.dockerHubUser}/two-tier-flask-app:latest"
                }
            }
        }
        stage("Deploy"){
            steps{
                sh "docker compose up -d --build flaskapp"
            }
        }
    }
    post {
        always {
            // Sends an email on every build outcome
            emailext (
                subject: "Build ${currentBuild.currentResult}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """Check console output at ${env.BUILD_URL} to view the logs.
                         Status: ${currentBuild.currentResult}""",
                to: 'shreerajpatil29@gmail.com'
            )
        }
        failure {
            // Triggers only if the build fails
            mail (
                to: 'shreerajpatil29@gmail.com',
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "The build failed. Please investigate immediately: ${env.BUILD_URL}"
            )
        }
    }
}
