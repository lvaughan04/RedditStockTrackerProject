package com.lvclones.RedditStockTracker.controllers;

import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import com.lvclones.RedditStockTracker.models.Post;
import com.lvclones.RedditStockTracker.services.PostService;
import java.util.List;


@Controller
public class PostController {
    
    private PostService postService;

    public PostController(PostService postService){
        this.postService = postService;
    }

    @QueryMapping
    public List<Post> getPostsBySubreddit(@Argument String subreddit){
        return postService.getPostsBySubreddit(subreddit);
    }

    @QueryMapping
    public List<Post> getAllPosts(){
        return postService.getAllPosts();
    }
}
