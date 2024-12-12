import os
import open3d as o3d


def read_obj(file_path):
    mesh_list = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith('.obj'):
                obj_file_path = os.path.join(root, file)
                mesh = o3d.io.read_triangle_mesh(obj_file_path)
                mesh_list.append(mesh)
    o3d.visualization.draw_geometries(mesh_list)


def read_ply_list(file_path):
    ply_list = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith('.ply'):
                ply_file_path = os.path.join(root, file)
                pcd = o3d.io.read_point_cloud(ply_file_path)
                ply_list.append(pcd)

    combined_pcd = o3d.geometry.PointCloud()
    for pcd in ply_list:
        combined_pcd += pcd
    o3d.io.write_point_cloud("model.ply", combined_pcd, write_ascii=True)
    o3d.visualization.draw_geometries([combined_pcd], window_name="大红鹰", width=1024, height=768)


def read_ply(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    o3d.visualization.draw_geometries([pcd], window_name="大红鹰", width=1024, height=768)


if __name__ == '__main__':
    # read_obj('F:\BaiduNetdiskDownload\OBJ\Data')
    # read_ply_list('F:\BaiduNetdiskDownload\PLY')
    read_ply('model.ply')
