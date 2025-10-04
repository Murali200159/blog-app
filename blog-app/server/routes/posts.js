const express = require('express');
const auth = require('../middleware/auth');
const { getPosts, getPost, createPost, updatePost, deletePost } = require('../controllers/postController');
const router = express.Router();

router.get('/', getPosts);
router.get('/:id', getPost);
router.post('/', auth, createPost);
router.put('/:id', auth, updatePost);
router.delete('/:id', auth, deletePost);

module.exports = router;