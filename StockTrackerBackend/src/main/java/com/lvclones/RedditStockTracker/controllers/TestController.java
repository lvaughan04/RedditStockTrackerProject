package com.lvclones.RedditStockTracker.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {

    @GetMapping("/testing")
    public String displayMessage() {
        // This will return a simple string when the root URL is accessed
        return "Hello, the root route is working!";
    }
}
