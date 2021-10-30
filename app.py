from flask import Flask, redirect,render_template,request,url_for
import pickle
model = open('model.pkl','rb')
Model = pickle.load(model)

scales = open('scale.pkl','rb')
scale = pickle.load(scales)


app = Flask('app')


@app.route('/',methods=['POST', 'GET'])
@app.route('/home',methods=['POST', 'GET'])
def hello_world():

  return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    
    if request.method == 'POST':
      cap_shape = request.form['cap-shape']
      cap_surface = request.form['cap-surface']
      cap_color = request.form['cap-color']
      bruises = request.form['bruises']
      odor = request.form['odor']
      gill_attachment = request.form['gill-attachment']
      gill_spacing = request.form['gill-spacing']
      gill_size = request.form['gill-size']
      gill_color = request.form['gill-color']
      stalk_shape = request.form['stalk-shape']
      stalk_root = request.form['stalk-root']
      stalk_surface_above_ring = request.form['stalk-surface-above-ring']
      stalk_surface_below_ring = request.form['stalk-surface-below-ring']
      stalk_color_above_ring = request.form['stalk-color-above-ring']
      stalk_color_below_ring = request.form['stalk-color-below-ring']
      veil_type = request.form['veil-type']
      veil_color = request.form['veil-color']
      ring_number = request.form['ring-number']
      ring_type = request.form['ring-type']
      spore_print_color = request.form['spore-print-color']
      population = request.form['population']
      habitat = request.form['habitat']

      features=[[cap_shape,cap_surface,cap_color,bruises,odor,gill_attachment,gill_spacing,gill_size,gill_color,stalk_shape,stalk_root,stalk_surface_above_ring,stalk_surface_below_ring,stalk_color_above_ring,stalk_color_below_ring,veil_type,veil_color,ring_number,ring_type,spore_print_color,population,habitat]]
      X_scale=scale.transform(features)

      predict=Model.predict(X_scale)

      if predict=='edible':
            return render_template('edible.html')
      
      elif predict=='poisonous':
            return render_template('Poisonous.html')

if __name__=='__main__':
  app.run(debug=True)
