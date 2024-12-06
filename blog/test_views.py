from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import CommentForm
from .models import Post, ReadLater

# Create your tests here.
class TestBlogViews(TestCase):


    def setUp(self):
        """Create a superuser and a blog post"""
        self.user = User.objects.create_superuser(
            username="myUsername", password="myPassword", email="test@test.com")
        self.post = Post.objects.create(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        """Verifies a single blog post containing a comment form is returned"""
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(
            reverse('post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment submitted and awaiting approval',
                      response.content)

    def test_add_to_read_later(self):
        """Test for adding a post to the Read Later list"""
        self.client.login(username='myUsername', password='myPassword')
        
        # Make the POST request to add the post to the Read Later list
        response = self.client.post(reverse('add_to_read_later', args=[self.post.slug]))

        # Assert that the response is a redirect (302)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect to the target page (typically the Read Later list page)
        response = self.client.get(reverse('read_later'))
        
        # Check that the success message is in the response content
        self.assertContains(response, "This post is successfully added to your Read Later list.")

    

    def test_remove_from_read_later(self):
        """Test for removing a post from the Read Later list"""
        self.client.login(username='myUsername', password='myPassword')
        
        # First, add the post to the Read Later list
        self.client.post(reverse('add_to_read_later', args=[self.post.slug]))
        
        # Now, make the POST request to remove the post from the Read Later list
        response = self.client.post(reverse('remove_from_read_later', args=[self.post.slug]))

        # Assert that the response is a redirect (302)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect to the target page (typically the Read Later list page)
        response = self.client.get(reverse('read_later'))
        
        # Check that the success message is in the response content
        self.assertContains(response, "This post has been removed from your Read Later list.")
    
    def test_upvote_post(self):
        """Test for upvoting a post"""
        self.client.login(username="myUsername", password="myPassword")
        
        # Upvote the post
        response = self.client.post(reverse('post_upvote', args=['blog-title']))
        
        # Assert redirect (302) after upvoting
        self.assertEqual(response.status_code, 302)
        
        # Fetch the updated post and check if the user is in the upvotes
        post = Post.objects.get(slug='blog-title')
        self.assertIn(self.user, post.upvotes.all())
        
        # Check if downvotes were removed if previously downvoted
        self.assertNotIn(self.user, post.downvotes.all())

    def test_upvote_removal(self):
        """Test for removing upvote (if already upvoted)"""
        self.client.login(username="myUsername", password="myPassword")
        
        # First upvote the post
        self.client.post(reverse('post_upvote', args=['blog-title']))
        
        # Now remove the upvote (should be removed when clicked again)
        response = self.client.post(reverse('post_upvote', args=['blog-title']))
        
        # Assert redirect (302) after removing upvote
        self.assertEqual(response.status_code, 302)
        
        # Fetch the updated post and check if the upvote was removed
        post = Post.objects.get(slug='blog-title')
        self.assertNotIn(self.user, post.upvotes.all())

    def  test_downvote_post(self):
        """Test for downvoting a post"""
        self.client.login(username="myUsername", password="myPassword")
        
        # Downvote the post
        response = self.client.post(reverse('post_downvote', args=['blog-title']))
        
        # Assert redirect (302) after downvoting
        self.assertEqual(response.status_code, 302)
        
        # Fetch the updated post and check if the user is in the downvotes
        post = Post.objects.get(slug='blog-title')
        self.assertIn(self.user, post.downvotes.all())
        
        # Check if upvotes were removed if previously upvoted
        self.assertNotIn(self.user, post.upvotes.all())

    def test_downvote_removal(self):
        """Test for removing downvote (if already downvoted)"""
        self.client.login(username="myUsername", password="myPassword")
        
        # First downvote the post
        self.client.post(reverse('post_downvote', args=['blog-title']))
        
        # Now remove the downvote (should be removed when clicked again)
        response = self.client.post(reverse('post_downvote', args=['blog-title']))
        
        # Assert redirect (302) after removing downvote
        self.assertEqual(response.status_code, 302)
        
        # Fetch the updated post and check if the downvote was removed
        post = Post.objects.get(slug='blog-title')
        self.assertNotIn(self.user, post.downvotes.all())

    