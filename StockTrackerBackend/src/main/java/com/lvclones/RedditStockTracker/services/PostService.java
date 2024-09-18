package com.lvclones.RedditStockTracker.services;

import org.springframework.stereotype.Service;
import java.util.List;
import com.lvclones.RedditStockTracker.repositories.PostRepository;
import com.lvclones.RedditStockTracker.models.Post;


@Service
public class PostService {

    private PostRepository postRepository;

    public PostService(PostRepository postRepository){
        this.postRepository = postRepository;
    }

    public List<Post> getPostsBySubreddit(String subreddit){
        return postRepository.findPostsBySubreddit(subreddit);
    }

    public List<Post> getAllPosts(){
        return postRepository.findAll();
    }
}
