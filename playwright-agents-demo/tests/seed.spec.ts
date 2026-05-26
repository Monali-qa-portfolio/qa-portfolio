import { test, expect } from '../fixtures';

// SEED TEST
// Bootstraps the environment for the Playwright agents.
// The Planner runs this first and uses it as the style example.
test('seed', async ({ todoPage }) => {
  await expect(todoPage.newTodoInput).toBeVisible();
});