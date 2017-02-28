import tensorflow as tf

new_checkpoint_vars = {}

reader = tf.train.NewCheckpointReader("im2txt/chk_point/model.ckpt-2000000")

for old_name in reader.get_variable_to_shape_map():
  new_name = old_name # Rename as desired
  new_checkpoint_vars[new_name] = tf.Variable(reader.get_tensor(old_name))

init = tf.global_variables_initializer()
saver = tf.train.Saver(new_checkpoint_vars)

with tf.Session() as sess:
  sess.run(init)
  saver.save(sess, "im2txt/chk_point/model-renamed.ckpt")