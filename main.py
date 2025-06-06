from scene_analyze import SceneAnalyze
from grouping import cluster_by_clip_and_dbscan, draw_clustered_objects

if __name__ == "__main__":
    # 1. Depth Estimation + Object Detection + Filtering
    analyze = SceneAnalyze(r'C:\IoT_project\segmentation_iot-1\dataset\val2017 (1)\val2017\000000000885.jpg') 
    # 'sample/sample.jpg'->'C:\IoT_project\segmentation_iot-1\dataset\val2017 (1)\val2017\000000000885.jpg'
    analyze.run()

    print("[DEBUG] 필터링된 객체 수:", len(analyze.filtered_objects))

    # 2. CLIP + DBSCAN Grouping
    grouped_objects = cluster_by_clip_and_dbscan(analyze.filtered_objects)
    draw_clustered_objects(analyze.image, grouped_objects)


    # console 출력
    for obj in grouped_objects:
        cid = obj["cluster_id"]
        name = obj["class_name"]
        depth = obj["depth"]
        center = obj["center"]
        print(f"[Cluster {cid}] {name} at {center}, depth={depth:.2f}")
