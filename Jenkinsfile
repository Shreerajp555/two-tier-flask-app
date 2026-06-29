pipeline{
    agent {label "dev"}
    stages{
        stage("code"){
            steps{
                git url:"https://github.com/Shreerajp555/two-tier-flask-app.git", branch: "main"
            }
        }
        stage("build"){
            steps{
                sh "docker build -t myapp ."
            }
        }
        stage("test"){
            steps{
                echo "code tested"
            }
        }
        stage("push to docker hub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: "dockerHubCreds",
                    passwordVariable: "dockerHubPass",
                    usernameVariable: "dockerHubUser"
                    )]){
                        sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                        sh "docker image tag myapp ${env.dockerHubUser}/two-tier-flask-app"
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
}
