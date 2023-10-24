#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const completedTasks = {};
    const todos = JSON.parse(body);

    for (const todo of todos) {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    }

    console.log(completedTasks);
  } else {
    console.log('error: ', error);
  }
});
