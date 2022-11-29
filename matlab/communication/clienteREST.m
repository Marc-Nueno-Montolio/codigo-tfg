function [res] = clienteREST(url, method, payload)
    base_url = 'http://127.0.0.1:5000';
    url = [base_url '/' url];   
    if method == "POST"
        options = weboptions('RequestMethod','post', 'MediaType','application/json');
        res = webwrite(url, payload, options);
    elseif method == "GET"
        options = weboptions('RequestMethod','get', 'MediaType','application/json');
        res = webread(url, options);
    end
end

