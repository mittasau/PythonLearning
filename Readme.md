### Developer Checklist Before Raising a PR

Before submitting a pull request (PR), ensure the following steps are completed:

1. **Code Quality Checks**  
   - [ ] Run local linting (e.g., ESLint, Prettier) and fix all issues.  
   - [ ] Perform a static code analysis (e.g., SonarQube scan) and resolve any critical issues.  
   - [ ] Ensure code follows the project's coding standards and best practices.  

2. **Documentation**  
   - [ ] Document the impact areas of the new code changes (e.g., APIs, database schema, UI).  
   - [ ] Update README or relevant documentation if necessary.  

3. **PR Mapping**  
   - [ ] Ensure the PR number maps to a specific feature/story/ticket (e.g., JIRA ticket or GitHub issue).  
   - [ ] Add a clear and concise description of the changes in the PR.  

4. **Testing**  
   - [ ] Write and run unit tests for new code.  
   - [ ] Perform integration testing if applicable.  
   - [ ] Ensure all existing tests pass.  

5. **Adherence to Best Practices**  
   - [ ] Follow SOLID principles and design patterns where applicable.  
   - [ ] Avoid hardcoding values; use configuration files or environment variables.  
   - [ ] Ensure proper error handling and logging.  

6. **Code Review**  
   - [ ] Self-review your code for readability and maintainability.  
   - [ ] Ensure the PR is small and focused on a single feature/bug fix.  

7. **Branch Management**  
   - [ ] Ensure the branch is up-to-date with the main branch (e.g., `main` or `develop`).  
   - [ ] Rebase or merge the latest changes if necessary.  

8. **Commit Messages**  
   - [ ] Write clear and descriptive commit messages.  
   - [ ] Follow the project's commit message conventions (e.g., semantic commit messages).  

---

**Note:** This checklist is intended to ensure high-quality contributions. Please follow it diligently before raising a PR.
