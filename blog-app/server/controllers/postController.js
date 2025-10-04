const Post = require('../models/Post');

const getPosts = async (req, res) => {
  const { search = '', page = 1, limit = 10 } = req.query;
  try {
    const query = {
      $or: [
        { title: { $regex: search, $options: 'i' } },
        { username: { $regex: search, $options: 'i' } },
      ],
    };
    const posts = await Post.find(query)
      .skip((page - 1) * limit)
      .limit(Number(limit));
    res.json(posts);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching posts', details: error.message });
  }
};

const getPost = async (req, res) => {
  try {
    const post = await Post.findById(req.params.id);
    if (!post) return res.status(404).json({ message: 'Post not found' });
    res.json(post);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching post', details: error.message });
  }
};

const createPost = async (req, res) => {
  const { title, imageURL, content } = req.body;
  try {
    const post = new Post({ title, imageURL, content, username: req.user.username });
    await post.save();
    res.status(201).json(post);
  } catch (error) {
    res.status(400).json({ message: 'Error creating post', details: error.message });
  }
};

const updatePost = async (req, res) => {
  try {
    const post = await Post.findById(req.params.id);
    if (!post) return res.status(404).json({ message: 'Post not found' });
    if (post.username !== req.user.username) {
      return res.status(403).json({ message: 'Not authorized' });
    }
    Object.assign(post, req.body);
    await post.save();
    res.json(post);
  } catch (error) {
    res.status(400).json({ message: 'Error updating post', details: error.message });
  }
};

const deletePost = async (req, res) => {
  try {
    const post = await Post.findById(req.params.id);
    if (!post) return res.status(404).json({ message: 'Post not found' });
    if (post.username !== req.user.username) {
      return res.status(403).json({ message: 'Not authorized' });
    }
    await post.remove();
    res.json({ message: 'Post deleted' });
  } catch (error) {
    res.status(400).json({ message: 'Error deleting post', details: error.message });
  }
};

module.exports = { getPosts, getPost, createPost, updatePost, deletePost };