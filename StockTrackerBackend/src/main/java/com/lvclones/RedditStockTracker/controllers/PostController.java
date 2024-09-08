package com.lvclones.RedditStockTracker.controllers;

import org.springframework.stereotype.Controller;

import com.lvclones.RedditStockTracker.models.Post;
import com.lvclones.RedditStockTracker.services.PostService;

@Controller
public class PostController {
    
    private PostService postService;

    public PostController(PostService postService){
        this.postService = postService;
    }
}
