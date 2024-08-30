def test_index_route(client):
    response = client.get('/')
    
    assert response.status_code == 200
    
    assert b'<meta name="current-view" content="editor">' in response.data
    
    assert b'Editor' in response.data
    assert b'Generate PDF' in response.data

def test_catch_all_route(client):
    response = client.get('/some/invalid/path')
    
    assert response.status_code == 302  # indicates a redirect
    
    assert response.location.endswith('/')
    
    redirected_response = client.get('/')
    assert redirected_response.status_code == 200
    assert b'<meta name="current-view" content="editor">' in redirected_response.data
    assert b'Editor' in redirected_response.data
    assert b'Generate PDF' in redirected_response.data