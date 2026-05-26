import { test, expect } from '../fixtures';

test.describe('TodoMVC - Adding Todos (Happy Path)', () => {

  test('Add a single valid todo', async ({ todoPage }) => {
    await todoPage.addTodo('Buy groceries');

    await expect(todoPage.todoItems).toHaveText(['Buy groceries']);
    await expect(todoPage.todoCount).toHaveText('1 item left');
    await expect(todoPage.newTodoInput).toHaveValue('');
  });

  test('Add multiple todos', async ({ todoPage }) => {
    await todoPage.addTodo('Buy groceries');
    await todoPage.addTodo('Walk the dog');
    await todoPage.addTodo('Pay bills');

    await expect(todoPage.todoItems).toHaveText([
      'Buy groceries',
      'Walk the dog',
      'Pay bills',
    ]);
    await expect(todoPage.todoCount).toHaveText('3 items left');
  });

});