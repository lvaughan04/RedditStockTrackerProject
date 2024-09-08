package com.lvclones.RedditStockTracker.services;

import org.springframework.stereotype.Service;

import com.lvclones.RedditStockTracker.repositories.PostRepository;

@Service
public class PostService {

    private PostRepository postRepository;

    public PostService(PostRepository postRepository){
        this.postRepository = postRepository;
    }
}
