// ==UserScript==
// @name         51job
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @include      https://ehire.51job.com/Candidate/*
// @require  https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js
// @grant        none
// ==/UserScript==

(
    function() {
    'use strict';
    // Your code here...
    setTimeout(
        function() {
            var $ = window.jQuery;
            var label = 0;
            function recordIdUrl() {
                console.dir($(".ls").html());
                console.dir("*************************一条完美的分隔符*************************");
                var nextPage = $(".Common_icon_caret_right_large");
                nextPage.click();
                label++;
            }
            var interval = setInterval(function() {
                if (label > 3) {
                    clearInterval(interval);
                    return;
                }
                recordIdUrl()
            }, Math.random() * 5000 + 10000)
        }, 5000);
    }
)

();
