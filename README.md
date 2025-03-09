🚀 GitHub Actions CI/CD Pipeline

✅ Task Completion Confirmation

I have successfully implemented a CI/CD pipeline using GitHub Actions for both code and Docker workflows.

📌 Repository Details

The repository follows a feature branching strategy using the feature/* pattern.

Each feature/* branch has its own GitHub Actions workflow file.

The development branch acts as the main integration branch.

⚙️ CI/CD Pipeline Configuration

🔹 Feature Branch Pipelines

Triggered automatically when new code is pushed to a feature/* branch.

Code-related pipelines include:

✅ Lint check

✅ Unit test

✅ Code quality check

✅ Dependency check

Docker-related pipelines include:

✅ Dockerfile check

✅ Docker image check

🔄 After successful execution pull request is created against the development branch.

🔹 Development Branch Pipeline (Release Pipeline)

Triggered whenever a new release is made from the development branch.

The release pipeline:

🚀 Builds the final Docker image.

🔖 Ensures the image name matches the tag name.

📤 Pushes the image to the Docker Hub repository.
