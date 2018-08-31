//@format
const express = require('express');
const app = express();
const path = require('path');

app.get('/yesterday', (req, res) => {
  var spawn = require('child_process').spawnSync;
  var process = spawn('python3', [
    '../../scripts/data_analysis_scripts/create_yesterday_report.py',
  ]);
  res.sendFile(
    path.join(__dirname, '../reports/yesterday_campaigns_data.html'),
  );
});

app.get('/7days', (req, res) => {
  var spawn = require('child_process').spawnSync;
  var process = spawn('python3', [
    '../../scripts/data_analysis_scripts/create_seven_report.py',
  ]);
  res.sendFile(path.join(__dirname, '../reports/seven_campaigns_data.html'));
});

app.get('/30days', (req, res) => {
  var spawn = require('child_process').spawnSync;
  var process = spawn('python3', [
    '../../scripts/data_analysis_scripts/create_thirty_report.py',
  ]);
  res.sendFile(path.join(__dirname, '../reports/thirty_campaigns_data.html'));
});

app.get('/90days', (req, res) => {
  var spawn = require('child_process').spawnSync;
  var process = spawn('python3', [
    '../../scripts/data_analysis_scripts/create_ninety_report.py',
  ]);
  res.sendFile(path.join(__dirname, '../reports/ninety_campaigns_data.html'));
});

app.get('/180days', (req, res) => {
  var spawn = require('child_process').spawnSync;
  var process = spawn('python3', [
    '../../scripts/data_analysis_scripts/create_oneeighty_report.py',
  ]);
  res.sendFile(
    path.join(__dirname, '../reports/oneeighty_campaigns_data.html'),
  );
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.listen('3000', () => {
  console.log(`dashboard running on port 3000...`);
});
