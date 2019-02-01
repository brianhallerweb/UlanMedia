//@format
const fs = require('fs');

// 2/1/19
// this code is a mess but it works. It adds p widgets to white/grey/black
// lists and cleans and maintains those lists in the process.
// One thing that might be confusing is that the global_status column shown on
// the web app always (whether in development or production) comes from ulanmedia.brianhaller.net.
// In development, adding to list only impacts the development white/grey/black
// lists. However the global_status column still comes from
// ulanmedia.brianhaller.net when in development.

function addToList(pWidgetID, listType) {
  const currentListStatus = getCurrentListStatus(pWidgetID);
  let message = '';
  if (isNaN(pWidgetID) || pWidgetID.trim() === '') {
    //test if p widget is number
    //this doesn't mean in the variable "type" sense.
    //pWidgetID is a string, but it needs to be a number in the "12345"
    //sense
    message = 'p widget not added to list - invalid id';
    return message;
  }
  for (let key in currentListStatus) {
    if (key === listType && currentListStatus[key] === true) {
      if (message === '') {
        message = `p widget already in ${listType} list`;
      } else {
        message += ` and  already in ${listType} list`;
      }
    } else if (key === listType && currentListStatus[key] === false) {
      writeToList(pWidgetID, key);
      if (message === '') {
        message = `p widget added to ${listType} list`;
      } else {
        message += ` and added to ${listType} list`;
      }
    } else if (currentListStatus[key] === true) {
      eraseFromList(pWidgetID, key);
      if (message === '') {
        message = `p widget erased from ${key} list`;
      } else {
        message += ` and erased from ${key} list`;
      }
    }
  }
  return message;
}

function writeToList(pWidgetID, listType) {
  // This function is kind of convoluted but it just adds a p widget id to a
  // list.
  // It handles the cases of extra white space or extra lines.
  let pWidgets = fs
    .readFileSync(`../../p_widget_lists/${listType}list.txt`, 'utf8')
    .trim()
    .split('\n');
  const pWidgetsWithoutBlankLines = [];
  for (let i = 0; i < pWidgets.length; i++) {
    if (pWidgets[i] !== '') {
      pWidgetsWithoutBlankLines.push(pWidgets[i].trim());
    }
  }
  const pWidgetsWithoughBlankLinesAndWithNewPWidgetID = pWidgetsWithoutBlankLines.concat(
    pWidgetID,
  );

  fs.writeFileSync(
    `../../p_widget_lists/${listType}list.txt`,
    pWidgetsWithoughBlankLinesAndWithNewPWidgetID.join('\n'),
  );
}

function eraseFromList(pWidgetID, listType) {
  let pWidgets = fs
    .readFileSync(`../../p_widget_lists/${listType}list.txt`, 'utf8')
    .trim()
    .split('\n');
  const pWidgetsWithoutBlankLines = [];
  for (let i = 0; i < pWidgets.length; i++) {
    if (pWidgets[i] !== '') {
      pWidgetsWithoutBlankLines.push(pWidgets[i].trim());
    }
  }
  const pWidgetsWithoutBlankLinesAndWithPWidgetIDRemoved = [];
  for (let i = 0; i < pWidgets.length; i++) {
    if (pWidgetsWithoutBlankLines[i] !== pWidgetID) {
      pWidgetsWithoutBlankLinesAndWithPWidgetIDRemoved.push(
        pWidgetsWithoutBlankLines[i],
      );
    }
  }

  fs.writeFileSync(
    `../../p_widget_lists/${listType}list.txt`,
    pWidgetsWithoutBlankLinesAndWithPWidgetIDRemoved.join('\n'),
  );
}

function getCurrentListStatus(pWidgetID) {
  const currentListStatus = {
    white: false,
    grey: false,
    black: false,
  };
  if (isInWhiteList(pWidgetID)) {
    currentListStatus.white = true;
  }
  if (isInGreyList(pWidgetID)) {
    currentListStatus.grey = true;
  }
  if (isInBlackList(pWidgetID)) {
    currentListStatus.black = true;
  }
  return currentListStatus;
}

function isInWhiteList(pWidgetID) {
  const pWidgets = fs
    .readFileSync(`../../p_widget_lists/whitelist.txt`, 'utf8')
    .trim()
    .split('\n');
  for (let id of pWidgets) {
    if (id === pWidgetID) {
      return true;
    }
  }
  return false;
}

function isInGreyList(pWidgetID) {
  const pWidgets = fs
    .readFileSync(`../../p_widget_lists/greylist.txt`, 'utf8')
    .trim()
    .split('\n');
  for (let id of pWidgets) {
    if (id === pWidgetID) {
      return true;
    }
  }
  return false;
}

function isInBlackList(pWidgetID) {
  const pWidgets = fs
    .readFileSync(`../../p_widget_lists/blacklist.txt`, 'utf8')
    .trim()
    .split('\n');
  for (let id of pWidgets) {
    if (id === pWidgetID) {
      return true;
    }
  }
  return false;
}

module.exports = addToList;
