// ==UserScript==
// @name         LaGou
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://easy.lagou.com/talent/search/list.htm?city=%E6%B7%B1%E5%9C%B3&keyword=rust&pageNo=1&show_id=8ce678228ced452296c6178a986fd2ab
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
            function handleInfo() {
                console.dir($(".resume-content").html());
                console.dir("*************************一条完美的分隔符*************************");
                label ++;
                var nextButton = $(".icon-lg-arrow-right");
                nextButton.click();
            }
            var interval = setInterval(function() {
                if (label > 4) {
                    clearInterval(interval);
                    return;
                }
                handleInfo()
            }, Math.random()*4000 + 5000)
        }, 5000);
    }
)

();
