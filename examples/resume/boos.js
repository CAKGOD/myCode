// ==UserScript==
// @name         ZHIPIN test
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.zhipin.com/web/boss/recommend
// @require  https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js
// @require https://raw.githubusercontent.com/eligrey/FileSaver.js/master/FileSaver.js
// @grant        none
// ==/UserScript==

(
    function() {
        'use strict';
        setTimeout(function() {
            var $ = window.jQuery;
            var myFrames = $(window.frames["recommendFrame"].document);
            var firstCard = myFrames.find(".card-inner")[0]
            firstCard.click();

            var label = 0;

            function handleInfo() {
                //console.log("*************");
                //return
                var resumeItemPopBox = $(myFrames).find(".resume-item-pop-box");
                //console.log("TODO: extract info from this resumeItemPopBox");
                var candidateName = resumeItemPopBox.find(".resume-item-pop-box")
                console.dir(candidateName.html());
                console.dir("*************************一条完美的分隔符*************************");
                label++;
                var nextButton = resumeItemPopBox.find(".resume-next");
                nextButton.click();
            }
            var interval = setInterval(function() {
                if (label > 4) {
                    clearInterval(interval);
                    return;
                }
                handleInfo()
            }, Math.random()*2000 + 8000)
        }, 5000);
    }
)

();
